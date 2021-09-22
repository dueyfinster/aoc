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
        List<String> ls = new ArrayList<>();
        ls.add(">");
        List<Day3.CoOrd> coOrd = d3.processInput(ls);
        assertEquals(2, d3.Part1(coOrd));
    }

    @Test
    @DisplayName("^>v< = 4")
    void part1VisitFourHouses() {
        Day3 d3 = new Day3();
        List<String> ls = new ArrayList<>();
        ls.add("^>v<");
        List<Day3.CoOrd> coOrd = d3.processInput(ls);
        assertEquals(4, d3.Part1(coOrd));
    }
    @Test
    @DisplayName("^v^v^v^v^v = 2")
    void part1VisitLucky2Houses() {
        Day3 d3 = new Day3();
        List<String> ls = new ArrayList<>();
        ls.add("^v^v^v^v^v");
        List<Day3.CoOrd> coOrd = d3.processInput(ls);
        assertEquals(2, d3.Part1(coOrd));
    }


    @Test
    @DisplayName("Input File = 2565")
    void part1ActualResult() throws IOException {
        Day3 d2 = new Day3();
        List<String> input = Utils.readInFile("Day3");
        List<Day3.CoOrd> coOrds = d2.processInput(input);
        assertEquals(2565, d2.Part1(coOrds));
    }

}