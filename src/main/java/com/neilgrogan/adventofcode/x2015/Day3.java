package com.neilgrogan.adventofcode.x2015;

import java.io.IOException;
import java.util.*;

public class Day3 {

    public static void main(String[] args) throws IOException {
        Day3 d3 = new Day3();
        List<String> input = Utils.readInFile("Day3");

        char[] firstLine = input.get(0).toCharArray();
        System.out.println("Day 3, Part 1: " + d3.Part1(firstLine));
        System.out.println("Day 3, Part 2: " + d3.Part2(firstLine));
    }

    public int Part1(char[] firstLine) {
        Set<CoOrd> coOrds = new HashSet<>();
        CoOrd coOrd = new CoOrd(0, 0);
        coOrds.add(coOrd);

        for(char c : firstLine){
            coOrd = processMove(coOrd, c);
            coOrds.add(coOrd);
        }

        return coOrds.size();
    }

    public int Part2(char[] firstLine) {
        Set<CoOrd> santaCoOrds =  new HashSet<>();
        Set<CoOrd> roboSantaCoOrds =  new HashSet<>();
        CoOrd sCoOrd = new CoOrd(0, 0);
        CoOrd rsCoOrd = new CoOrd(0, 0);
        santaCoOrds.add(sCoOrd);
        roboSantaCoOrds.add(rsCoOrd);

        for(int i=0; i< firstLine.length; i++){
            if(i % 2 ==0){
                sCoOrd = processMove(sCoOrd, firstLine[i]);
                santaCoOrds.add(sCoOrd);
            }else{
                rsCoOrd = processMove(rsCoOrd, firstLine[i]);
                roboSantaCoOrds.add(rsCoOrd);
            }
        }

        santaCoOrds.addAll(roboSantaCoOrds);

        return santaCoOrds.size();
    }


    private CoOrd processMove(CoOrd coOrd, char c){
        coOrd = new CoOrd(coOrd.getX(), coOrd.getY());
        switch (c) {
            case '^' -> coOrd.increaseY();
            case 'v' -> coOrd.decreaseY();
            case '>' -> coOrd.increaseX();
            case '<' -> coOrd.decreaseX();
            default -> {
            }
        }
        return coOrd;
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
