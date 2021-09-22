package com.neilgrogan.adventofcode.x2015;

import java.io.IOException;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day5 {

    public static void main(String[] args) throws IOException {
        Day5 d5 = new Day5();
        List<String> input = Utils.readInFile("Day5");
        System.out.println("Day 5, Part 1: " + d5.part1(input));
        System.out.println("Day 5, Part 2: " + d5.part2(input));
    }

    public int part1(List<String> inputs){
        int count = 0;
        for(String input : inputs){
            if(contains3Vowels(input) && containsRepeatingChars(input) && missingbadChars(input)){
                count++;
            }
        }
        return count;
    }

    public int part2(List<String> inputs){
        return 0;
    }

    private boolean contains3Vowels(String input){
        Pattern vowels = Pattern.compile("([aeiou])");

        Matcher countVowels = vowels.matcher(input);

        long count = countVowels.results().count();

        return count >= 3;
    }

    private boolean containsRepeatingChars(String input){
        Pattern repeatChars = Pattern.compile("([a-z])(\\1)+");

        Matcher matchRepeatChars = repeatChars.matcher(input);

        long count = matchRepeatChars.results().count();

        return count >= 1;
    }

    private boolean missingbadChars(String input){
        List<String> list = Arrays.asList("ab", "cd", "pq", "xy");

        for (String s : list){
            if(input.contains(s)){
                return false;
            }
        }
        return true;
    }
}
