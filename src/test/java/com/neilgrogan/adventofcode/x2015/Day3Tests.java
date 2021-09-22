package com.neilgrogan.adventofcode.x2015;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Day3Tests {

    @Test
    @DisplayName("> = 2")
    void part1VisitTwoHouses() {
        Day3 d3 = new Day3();
        char[] firstLine = {'>'};
        assertEquals(2, d3.Part1(firstLine));
    }

    @Test
    @DisplayName("^>v< = 4")
    void part1VisitFourHouses() {
        Day3 d3 = new Day3();
        char[] firstLine = {'"','^','>','v','<'};
        assertEquals(4, d3.Part1(firstLine));
    }
    @Test
    @DisplayName("^v^v^v^v^v = 2")
    void part1VisitLucky2Houses() {
        Day3 d3 = new Day3();
        char[] firstLine = {'^','v','^','v','^','v','^','v','^','v'};
        assertEquals(2, d3.Part1(firstLine));
    }


    @Test
    @DisplayName("Input File = 2565")
    void part1ActualResult() throws IOException {
        Day3 d3 = new Day3();
        List<String> input = Utils.readInFile("Day3");
        char[] firstLine = input.get(0).toCharArray();
        assertEquals(2565, d3.Part1(firstLine));
    }


    @Test
    @DisplayName("^v = 3")
    void part2VisitThreeHouses() {
        Day3 d3 = new Day3();
        char[] firstLine = {'^', 'v'};
        assertEquals(3, d3.Part2(firstLine));
    }

    @Test
    @DisplayName("^>v< = 3")
    void part2VisitThreeHouses2() {
        Day3 d3 = new Day3();
        char[] firstLine = {'^','>','v','<'};
        assertEquals(3, d3.Part2(firstLine));
    }

    @Test
    @DisplayName("^v^v^v^v^v = 11")
    void part2VisitElevenHouses() {
        Day3 d3 = new Day3();
        char[] firstLine = {'^','v','^','v','^','v','^','v','^','v'};
        assertEquals(11, d3.Part2(firstLine));
    }

    @Test
    @DisplayName("Input File = 2639")
    void part2ActualResult() throws IOException {
        Day3 d3 = new Day3();
        List<String> input = Utils.readInFile("Day3");
        char[] firstLine = input.get(0).toCharArray();
        assertEquals(2639, d3.Part2(firstLine));
    }

}