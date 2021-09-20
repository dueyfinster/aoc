package com.neilgrogan.adventofcode.x2015;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

class Day1Tests {

    @Test
    @DisplayName("(()) = 0")
    void part1bracketsCancelOut() {
        Day1 d1 = new Day1();
        assertEquals(0, d1.Part1("(())"));
    }

    @Test
    @DisplayName("Input File = 280")
    void part1ActualResult() throws IOException {
        Day1 d1 = new Day1();
        Path path = Paths.get("src/main/resources/com/neilgrogan/adventofcode/x2015/Day1.txt");
        String input = Files.readAllLines(path).get(0);
        assertEquals(280, d1.Part1(input));
    }


    @Test
    @DisplayName("(())) = 5")
    void part2LastIndexBasementFloor() {
        Day1 d1 = new Day1();
        assertEquals(5, d1.Part2("(()))"));
    }

    @Test
    @DisplayName("Input File = 1797")
    void part2ActualResult() throws IOException {
        Day1 d1 = new Day1();
        Path path = Paths.get("src/main/resources/com/neilgrogan/adventofcode/x2015/Day1.txt");
        String input = Files.readAllLines(path).get(0);
        assertEquals(1797, d1.Part2(input));
    }

}