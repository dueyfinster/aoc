package com.neilgrogan.adventofcode.x2015;

import java.io.IOException;
import java.util.*;

public class Day3 {

    public static void main(String[] args) throws IOException {
        Day3 d3 = new Day3();
        List<String> input = Utils.readInFile("Day3");
        List<CoOrd> coOrds = d3.processInput(input);
        System.out.println("Day 3, Part 1: " + d3.Part1(coOrds));
        System.out.println("Day 3, Part 2: " + d3.Part2(coOrds));
    }

    public int Part1(List<CoOrd> coOrds) {
        Set<CoOrd> set = new HashSet<>(coOrds);
        //int[] arrays = coOrds.stream().map(CoOrdinate::getArray).distinct();
       // return (int) coOrds.stream().map(CoOrdinate::getArray).distinct().count();
        return set.size();
    }

    public int Part2(List<Day3.CoOrd> coOrds) {
        return 0;
    }


    public List<CoOrd> processInput(List<String> input){
        List<CoOrd> coOrds = new ArrayList<>();
        char[] firstLine = input.get(0).toCharArray();
        CoOrd coOrd = new CoOrd(0, 0);
        coOrds.add(coOrd);

        for(char c : firstLine){
            coOrd = new CoOrd(coOrd.getX(), coOrd.getY());
            if(c == '^'){
                coOrd.increaseY();
            }else if(c == 'v'){
                coOrd.decreaseY();
            }else if(c == '>'){
               coOrd.increaseX();
            }else if(c == '<'){
                coOrd.decreaseX();
            }
            coOrds.add(coOrd);
        }
        return coOrds;
    }

    public class CoOrd{
        int x, y;

        CoOrd(int x,int y){
            this.x = x;
            this.y = y;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }

        public void increaseY(){
            this.y = y + 1;
        }

        public void decreaseY(){
            this.y = y - 1;
        }

        public void increaseX(){
            this.x = x + 1;
        }

        public void decreaseX(){
            this.x = x - 1;
        }


        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            CoOrd coOrd = (CoOrd) o;
            return x == coOrd.x && y == coOrd.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }
}
