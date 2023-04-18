from cassandra.cluster import Cluster
import pandas as pd

class CassandraConnector:

    def __init__(self, client_id, client_secret, token):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = token

    try:
        def connect(self):
        cloud_config= {
                'secure_connect_bundle': 'secure-connect-clusteringineuron.zip'
        }
        auth_provider = PlainTextAuthProvider(self.client_id, self.client_secret, self.token)
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        session = cluster.connect()
        return session

        def create_keyspace(self, session, keyspace):
            session.execute(f"CREATE KEYSPACE IF NOT EXISTS {keyspace} WITH replication = {{'class': 'NetworkTopologyStrategy', 'datacenter1': '1'}}")

        def create_table(self, session, keyspace, table, columns):
            query = f"CREATE TABLE IF NOT EXISTS {keyspace}.{table} ("
            for col_name, col_type in columns.items():
                query += f"{col_name} {col_type},"
            query = query[:-1] + ")"
            session.execute(query)

        def insert_data_from_csv(self, session, keyspace, table, filepath):
            df = pd.read_csv(filepath)
            columns = df.dtypes.to_dict()
            self.create_table(session, keyspace, table, columns)
            for row in df.itertuples():
                query = f"INSERT INTO {keyspace}.{table} VALUES ("
                for col in df.columns:
                    value = row.__getattribute__(col)
                    if isinstance(value, str):
                        value = f"'{value}'"
                    query += f"{value},"
                query = query[:-1] + ")"
                session.execute(query)
    except Exception as e:
        print("An error has occured:", e)


client_id = "ASJMcNNrIPPQurIbXJSWMYUw"
client_secret = "6EgLxMe,7FUdSS2RLT08X4HfrZs6t312WcvR4OaYXsQ8BSPZg_LiEI2Axn+Z3HHADbl+5Ak7S7lufgq.cI0bFZq7UDTH9nnRAli.HygUJkT+Za6RZHDzoNq8fqhOmOCF"
token = "AstraCS:ASJMcNNrIPPQurIbXJSWMYUw:cc13a5fb0004d00a6368355fdc1c4618167620711279c52e79e6bbb953dc273b"
connector = CassandraConnector(client_id, client_secret, token)
session = connector.connect()

keyspace = "ineuroncluster"
table = "clusteringtable"
filepath = "C:/Users/HP/Customer_Clustering/Customer_Segmentation_Clustering/datasets/Train.csv"

connector.insert_data_from_csv(session, keyspace, table, filepath)
