import psycopg2
from rich import print
from ..core.interfaces import Sink
from typing import Any
import pandas as pd

class PostgresSink(Sink):
    def __init__(self, host: str, port: int, database: str, user: str, password: str, table_name: str ="weather_data", debug: bool = False, verbose: bool = False) -> None:
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.table_name = table_name
        self.debug = debug
        self.verbose = verbose


    def load(self, data: Any) -> None:
        conn = None
        cursor = None
        
        if self.verbose:
            print(f"[green]Connecting to PostgreSQL database:[/green]")
        
        try:
        
            conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            
            if self.debug:
                print(f"[yellow]Connected to PostgreSQl using '{self.user} - {self.database} - {self.host}:{self.port}'[/yellow]")
            
            cursor = conn.cursor()
            
            self._create_table(cursor)
                        
            #Region Insert Data
            self._insert_data(conn, cursor, data)
            #endregion
        
        except psycopg2.OperationalError as e:
            print(f"[red]X Connection error:[/red] {e}")
            raise
        
        except psycopg2.Error as e:
            print(f"[red]X Database error:[/red] {e}")
            raise
        
                    
        except Exception as e:
            print(f"[red]X Unexpected error in inserting data:[/red] {e}")
            raise
        
        finally:
            
            # garante que fecha a conexao mesmo se der erro
            if cursor:               
                cursor.close()
            if conn:
                conn.close()
            
            if self.verbose:
                print(f"[green]Connection closed.[/green]")
            
    
    def _create_table(self, cursor) -> None:
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            id SERIAL PRIMARY KEY,
            time TIMESTAMP NOT NULL,
            lat FLOAT NOT NULL,
            lon FLOAT NOT NULL,
            temp FLOAT,
            temp_f FLOAT,
            temp_category VARCHAR(20),
            humidity INTEGER,
            hour INTEGER,
            day_of_week INTEGER,
            is_daytime INTEGER,
            heat_index FLOAT,
            UNIQUE (time, lat, lon) -- to avoid duplicate entries for the same timestamp and location (chave composta)
        );
        """
        cursor.execute(create_table_query)
        
        if self.verbose:
            print(f"[green]Table '{self.table_name}' ensured to exist.[/green]")
            
    def _insert_data(self, conn, cursor, data: pd.DataFrame) -> None:
        insert_query = f"""
        INSERT INTO {self.table_name} (time, lat, lon, temp, humidity, temp_f, temp_category, hour, day_of_week, is_daytime, heat_index)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (time,lat,lon) DO UPDATE SET
            temp = EXCLUDED.temp,
            temp_f = EXCLUDED.temp_f,
            temp_category = EXCLUDED.temp_category,
            humidity = EXCLUDED.humidity,
            hour = EXCLUDED.hour,
            day_of_week = EXCLUDED.day_of_week,
            is_daytime = EXCLUDED.is_daytime,
            heat_index = EXCLUDED.heat_index;
        """
        
        tuples = [tuple(x) for x in data.to_numpy()]
        cursor.executemany(insert_query, tuples)
        conn.commit()
        
        if self.verbose:
            print(f"[green]Inserted/Updated {len(tuples)} rows into '{self.table_name}'.[/green]")
        
        if self.debug:
            print(f"[yellow]Rows affected: {cursor.rowcount}[/yellow]")
        