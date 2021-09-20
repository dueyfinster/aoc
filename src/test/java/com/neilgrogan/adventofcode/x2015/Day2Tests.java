package com.neilgrogan.adventofcode.x2015;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.util.List;

class Day2Tests {

    @Test
    @DisplayName("2*3*4 Shape Dimensions is = 52")
    void part1DimensionSurfaceAreaTest() {
        Day2.Dimension dim = new Day2.Dimension(2,3,4);
        assertEquals(52, dim.getSurfaceArea());
    }

    @Test
    @DisplayName("2*3*4 Shape Total is = 58")
    void part1DimensionTotalAreaTest() {
        Day2.Dimension dim = new Day2.Dimension(2,3,4);
        assertEquals(58, dim.getTotal());
    }

    @Test
    @DisplayName("Input File = 1606483")
    void part1ActualResult() throws IOException {
        Day2 d2 = new Day2();
        List<String> input = Utils.readInFile("Day2");
        List<Day2.Dimension> dimensions = d2.processInput(input);
        assertEquals(1606483, d2.Part1(dimensions));
    }

}