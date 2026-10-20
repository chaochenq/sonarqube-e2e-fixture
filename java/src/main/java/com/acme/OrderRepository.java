package com.acme;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import javax.crypto.Cipher;

public class OrderRepository {
    private final Connection connection;

    public OrderRepository(Connection connection) {
        this.connection = connection;
    }

    public ResultSet byCustomer(String customer) throws SQLException {
        Statement statement = connection.createStatement();
        return statement.executeQuery("SELECT id, total FROM orders WHERE customer = '" + customer + "'");
    }

    public Cipher legacyCipher() throws Exception {
        return Cipher.getInstance("DES/ECB/PKCS5Padding");
    }
}
