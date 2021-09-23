package com.neilgrogan.adventofcode.x2015;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day6 {
    enum State {ON, OFF, TOGGLE}

    public static void main(String[] args) throws IOException {
        Day6 d6 = new Day6();
        List<String> input = Utils.readInFile("Day6");
        System.out.println("Day 6, Part 1: " + d6.part1(input));
        System.out.println("Day 6, Part 2: " + d6.part2(input));
    }

    public int part1(List<String> input){
        List<Action> actions = processStringsToActions(input);
        int[][] lights = new int[1000][1000];

        for(Action action : actions){
            processAction(lights, action);
        }

        return (int) Arrays.stream(lights)
                .flatMapToInt(Arrays::stream)
                .filter(i -> i == 1)
                .count();
    }

    public int part2(List<String> input){
        return 0;
    }

    private List<Action> processStringsToActions(List<String> lines){
        Pattern repeatChars = Pattern.compile("(on|off|toggle).(\\d{1,3})[,](\\d{1,3})[a-z\\s]+(\\d{1,3})[,](\\d{1,3})");
        List<Action> actions = new ArrayList<>();
        for(String line : lines){
            Matcher m = repeatChars.matcher(line);
            if(m.find()){
                String action = m.group(1);
                int startX = Integer.parseInt(m.group(2));
                int startY = Integer.parseInt(m.group(3));
                int endX = Integer.parseInt(m.group(4));
                int endY = Integer.parseInt(m.group(5));

                actions.add(new Action(action, startX, startY, endX, endY));
            }
        }
        return actions;
    }

    private void processAction(int[][] lights, Action a) {

        for (int i = a.start.x; i <= a.end.x; i++) {
            for (int j = a.start.y; j <= a.end.y; j++) {
                if (a.state == State.ON) {
                    lights[i][j] = 1;
                } else if (a.state == State.OFF) {
                    lights[i][j] = 0;
                } else {
                    lights[i][j] = lights[i][j] ^ 1; //XOR to flip the value
                }
            }
        }
    }

        public class Action {
            private State state;
            private CoOrd start;
            private CoOrd end;

            Action(String state, int startX, int startY, int endX, int endY) {
                this.state = convertState(state);
                this.start = new CoOrd(startX,startY);
                this.end = new CoOrd(endX,endY);
            }

            public State getState() {
                return state;
            }

            public CoOrd getStart() {
                return start;
            }

            public CoOrd getEnd() {
                return end;
            }

            private State convertState(String s_state) {
                switch (s_state) {
                    case "on" -> {
                        return State.ON;
                    }
                    case "off" -> {
                        return State.OFF;
                    }
                    case "toggle" -> {
                        return State.TOGGLE;
                    }
                    default -> {
                    }
                }

                return null;
            }

            public class CoOrd {
                int x, y;

                CoOrd(int x, int y) {
                    this.x = x;
                    this.y = y;
                }

                public int getX() {
                    return x;
                }

                public int getY() {
                    return y;
                }
            }
        }
    }