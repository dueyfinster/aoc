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

  test "part1 - test input" do
    input = """
    7mmmfrrdcqs
    fivegfk5sixeight7pt14
    19two
    339bfrsfdbbxv32zxjxkflknlvsq
    51
    """

    result = part1(input)

    assert result == 142
  end

  @tag :skip
  test "part2" do
    input = nil
    result = part2(input)

    assert result
  end
end
