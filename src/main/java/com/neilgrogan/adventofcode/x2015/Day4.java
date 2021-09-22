package com.neilgrogan.adventofcode.x2015;

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Day4 {

    public static void main(String[] args){
        Day4 d4 = new Day4();
        System.out.println("Day 4, Part 1: " + d4.part1("iwrupvqb"));
        System.out.println("Day 4, Part 2: " + d4.part2("iwrupvqb"));
    }

    public int part1(String input) {
        try{
            boolean found = false;
            MessageDigest md = MessageDigest.getInstance("MD5");
            int i = 0 ;
            String number = input + i;
            do{
                md.update(number.getBytes());
                byte[] digest = md.digest();
                char[] chars = toHex(digest).toCharArray();
                int count = 0;
                if(chars[0] == 48 && chars[1] == 48 && chars[2] == 48 && chars[3] == 48 && chars[4] == 48){
                    found = true;
                    break;
                }
                i++;
                number = input + i;

            }while(!found);
            return i;
        }catch(NoSuchAlgorithmException e){
            System.out.println("MD5 Algorithm not found!");
        }

        return 0;
    }

    public int part2(String input){
        try{
            boolean found = false;
            MessageDigest md = MessageDigest.getInstance("MD5");
            int i = 0 ;
            String number = input + i;
            do{
                md.update(number.getBytes());
                byte[] digest = md.digest();
                char[] chars = toHex(digest).toCharArray();
                int count = 0;
                if(chars[0] == 48 && chars[1] == 48 && chars[2] == 48 && chars[3] == 48 && chars[4] == 48 && chars[5] == 48){
                    found = true;
                    break;
                }
                i++;
                number = input + i;

            }while(!found);
            return i;
        }catch(NoSuchAlgorithmException e){
            System.out.println("MD5 Algorithm not found!");
        }

        return 0;
    }

    public static String toHex(byte[] bytes) {
        BigInteger bi = new BigInteger(1, bytes);
        return String.format("%0" + (bytes.length << 1) + "X", bi);
    }
}
