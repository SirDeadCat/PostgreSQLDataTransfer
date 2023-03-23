using System;
using System.Data;
using MySql.Data.MySqlClient;

namespace MySQLDataTransfer
{
    class Program
    {
        public static void TransferData(string srcConnectionString, string destConnectionString, string tableName)
        {
            using (var srcConnection = new MySqlConnection(srcConnectionString))
            using (var destConnection = new MySqlConnection(destConnectionString))
            {
                srcConnection.Open();
                destConnection.Open();

                // Получение данных из исходной базы данных
                var selectCommand = new MySqlCommand($"SELECT * FROM {tableName};", srcConnection);
                var dataReader = selectCommand.ExecuteReader();

                // Создание команды вставки для целевой базы данных
                var insertCommand = new MySqlCommand();
                insertCommand.Connection = destConnection;

                while (dataReader.Read())
                {
                    var values = new object[dataReader.FieldCount];
                    dataReader.GetValues(values);

                    var valuesStr = string.Join(", ", values);
                    insertCommand.CommandText = $"INSERT INTO {tableName} VALUES ({valuesStr});";
                    insertCommand.ExecuteNonQuery();
                }

                srcConnection.Close();
                destConnection.Close();
            }
        }

        static void Main(string[] args)
        {
            string sourceConnectionString = "server=source_host;database=source_db;uid=user;pwd=password;";
            string destinationConnectionString = "server=destination_host;database=destination_db;uid=user;pwd=password;";
            string tableToTransfer = "table_name";

            TransferData(sourceConnectionString, destinationConnectionString, tableToTransfer);
        }
    }
}
