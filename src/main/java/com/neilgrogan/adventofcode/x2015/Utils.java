package com.neilgrogan.adventofcode.x2015;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

class Utils {
    public static String sPath = "src/main/resources/com/neilgrogan/adventofcode/x2015/%s.txt";

    public static List<String> readInFile(String fileName) throws IOException {
        Path path = Paths.get(String.format(sPath, fileName));
        return  Files.readAllLines(path);
    }
}