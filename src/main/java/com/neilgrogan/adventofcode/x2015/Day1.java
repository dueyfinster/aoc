package com.neilgrogan.adventofcode.x2015;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class Day1 {

    public static void main(String[] args) throws IOException {
        Day1 d1 = new Day1();
        String input = Utils.readInFile("Day1").get(0);
        System.out.println("Day 1, Part 1: " + d1.Part1(input));
        System.out.println("Day 1, Part 2: " + d1.Part2(input));
    }
    public int Part1(String input) {
        long openBrackets = input.chars().filter(x -> x == '(').count();
        long closedBrackets = input.chars().filter(x -> x == ')').count();
        return (int) (openBrackets - closedBrackets);
    }

    public int Part2(String input) {
        char[] c = input.toCharArray();
        int runningTotal = 0;
        for(int i=0; i<c.length; i++){
            if(c[i] =='('){
                runningTotal += 1;
            }else if(c[i] ==')'){
                runningTotal -= 1;
            }

            if(runningTotal == -1){
                return i+1;
            }
        }
        return 0;
    }

    private static String readInFile() throws IOException {
        Path path = Paths.get("src/main/resources/2015/Day1.txt");
        String input = Files.readAllLines(path).get(0);
        return input;
    }
}