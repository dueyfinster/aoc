defmodule AdventOfCode.Day01Test do
  use ExUnit.Case

  import AdventOfCode.Day01

  test "part1 - sample input" do
    input = """
    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
    """

    result = part1(input)

    assert result == 142
  end

  test "part1 - only number input" do
    input = """
    51
    """

    result = part1(input)

    assert result == 51
  end

  test "part2 - sample input" do
    input = """
    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen
    """
    result = part2(input)

    assert result == 281
  end
end
