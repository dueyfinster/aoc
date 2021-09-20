package com.neilgrogan.adventofcode.x2015;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

class Day2 {

    public static void main(String[] args) throws IOException {
        Day2 d2 = new Day2();
        List<String> input = Utils.readInFile("Day2");
        List<Dimension> dimensions = d2.processInput(input);
        System.out.println("Day 1, Part 1: " + d2.Part1(dimensions));
        System.out.println("Day 1, Part 2: " + d2.Part2(dimensions));
    }


    public int Part1(List<Dimension> dimensions) {
        int res = dimensions.stream().mapToInt(x -> x.getTotal()).sum();
        return res;
    }

    public int Part2(List<Dimension> dimensions) {
        return 0;
    }


    public List<Dimension> processInput(List<String> input){
        List<Dimension> dimensions = new ArrayList<Dimension>();
        Pattern p = Pattern.compile("([\\d]{1,3})[x]([\\d]{1,3})[x]([\\d]{1,3})");

        for(String line : input){
            Matcher m = p.matcher(line);
            if (m.find()) {
                int length = Integer.parseInt(m.group(1));
                int width = Integer.parseInt(m.group(2));
                int height = Integer.parseInt(m.group(3));
                dimensions.add(new Dimension(length, width, height));
            }
        }

        return dimensions;
    }

    static class Dimension{

        int length, width, height;
        int[] sides = new int[3];

        Dimension(int length, int width, int height){
            this.length = length;
            this.width = width;
            this.height = height;
            this.sides[0] = length*width;
            this.sides[1] = width*height;
            this.sides[2] = height*length;
        }

        public int getSurfaceArea(){
            return Arrays.stream(sides).map(x -> x * 2).sum();
        }

        public int getTotal(){
            int sumSides = getSurfaceArea();
            int slack = Arrays.stream(sides)
                    .min()
                    .getAsInt();

            return sumSides + slack;
        }
    }
}