package com.oreilly.books;

import java.io.IOException;
import java.io.Reader;
import java.io.StringReader;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVRecord;

public class App {
    public static void main( String[] args ) throws IOException {
        Reader in = new StringReader("a,b,c");
        for (CSVRecord record : CSVFormat.DEFAULT.parse(in)) {
            for (String field : record) {
                System.out.print("\"" + field + "\", ");
            }
            System.out.println();
        }
    }
}
