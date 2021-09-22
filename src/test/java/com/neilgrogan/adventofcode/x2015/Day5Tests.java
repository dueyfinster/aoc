package com.neilgrogan.adventofcode.x2015;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Day5Tests {

    @Test
    @DisplayName("ugknbfddgicrmopn = 1")
    void part1ExampleGoodString() {
        Day5 d5 = new Day5();
        List<String> inputs = List.of("ugknbfddgicrmopn");
        assertEquals(1, d5.part1(inputs));
    }

    @Test
    @DisplayName("aaa = 1")
    void part1ThreeAs() {
        Day5 d5 = new Day5();
        List<String> inputs = List.of("aaa");
        assertEquals(1, d5.part1(inputs));
    }

    @Test
    @DisplayName("jchzalrnumimnmhp = 0")
    void part1NaughtyNoDoubleLetter() {
        Day5 d5 = new Day5();
        List<String> inputs = List.of("jchzalrnumimnmhp");
        assertEquals(0, d5.part1(inputs));
    }

    @Test
    @DisplayName("haegwjzuvuyypxyu = 0")
    void part1NaughtyHasStringXY() {
        Day5 d5 = new Day5();
        List<String> inputs = List.of("haegwjzuvuyypxyu");
        assertEquals(0, d5.part1(inputs));
    }

    @Test
    @DisplayName("dvszwmarrgswjxmb = 0")
    void part1NaughtyHasOnlyOneVowel() {
        Day5 d5 = new Day5();
        List<String> inputs = List.of("dvszwmarrgswjxmb");
        assertEquals(0, d5.part1(inputs));
    }

    @Test
    @DisplayName("Input File = 255")
    void part1ActualResult() throws IOException {
        Day5 d5 = new Day5();
        List<String> input = Utils.readInFile("Day5");
        assertEquals(255, d5.part1(input));
    }


}