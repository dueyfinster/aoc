# 2023 Day 1
# Started: 01/05/24
# Finished: Part 1 - 01/05/24
# Problem summary:
# Get the numbers from input, concat first/last & add.
defmodule AdventOfCode.Day01 do

  def part1(input) do
    input
    |> String.split("\n", trim: true)
    |> Enum.map(&Regex.scan(~r/\d/, &1))
    |> Enum.map(&List.flatten(&1))
    |> Enum.map(&extract_first_and_last/1)
    |> Enum.map(&List.to_string(&1))
    |> Enum.map(&String.to_integer/1)
    |> IO.inspect()
    |> Enum.sum()
  end

  defp extract_first_and_last([]), do: nil
  defp extract_first_and_last(list) do
    [first | rest] = list
    last = List.first(Enum.reverse(rest))
    [first, last || first]
  end

  def part2(_args) do
  end

end
