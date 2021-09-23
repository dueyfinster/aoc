package com.neilgrogan.adventofcode.x2015;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Day6Tests {

    @Test
    @DisplayName("turn on 0,0 through 999,999 = every light on")
    void part1ExampleGoodString() {
        Day6 d6 = new Day6();
        List<String> inputs = List.of("turn on 0,0 through 999,999");
        assertEquals(1_000_000, d6.part1(inputs));
    }

    @Test
    @DisplayName("toggle 0,0 through 999,0 = first row lights on")
    void part1ToggleFirstRow() {
        Day6 d6 = new Day6();
        List<String> inputs = List.of("toggle 0,0 through 999,0");
        assertEquals(1000, d6.part1(inputs));
    }

    @Test
    @DisplayName("turn off 499,499 through 500,500 = 4 lights not on")
    void part1Middle4lightsOff() {
        Day6 d6 = new Day6();
        List<String> inputs = List.of("turn on 0,0 through 999,999", "turn off 499,499 through 500,500");
        assertEquals(999_996, d6.part1(inputs));
    }

    @Test
    @DisplayName("Input File = 569999")
    void part1ActualResult() throws IOException {
        Day6 d6 = new Day6();
        List<String> input = Utils.readInFile("Day6");
        assertEquals(569999, d6.part1(input));
    }
}