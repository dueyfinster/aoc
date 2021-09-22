package com.neilgrogan.adventofcode.x2015;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.security.NoSuchAlgorithmException;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Day4Tests {

    @Test
    @DisplayName("abcdef = 609043")
    void part1FirstExampleHash() {
        Day4 d4 = new Day4();
        assertEquals(609043, d4.part1("abcdef"));
    }

    @Test
    @DisplayName("pqrstuv = 1048970")
    void part1SecondExampleHash() {
        Day4 d4 = new Day4();
        assertEquals(1048970, d4.part1("pqrstuv"));
    }

    @Test
    @DisplayName("iwrupvqb = 346386")
    void part1Actual() {
        Day4 d4 = new Day4();
        assertEquals(346386, d4.part1("iwrupvqb"));
    }

    @Test
    @DisplayName("iwrupvqb = 9958218")
    void part2Actual() {
        Day4 d4 = new Day4();
        assertEquals(9958218, d4.part2("iwrupvqb"));
    }
}