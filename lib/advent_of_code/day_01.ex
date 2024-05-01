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
    |> Enum.sum()
  end

  defp extract_first_and_last([]), do: nil

  defp extract_first_and_last(list) do
    [first | rest] = list
    last = List.first(Enum.reverse(rest))
    [first, last || first]
  end

  def part2(input) do
    input
    |> String.split("\n", trim: true)
    |> Enum.map(&replace_numbers/1)
    |> Enum.map(&Regex.scan(~r/\d/, &1))
    |> Enum.map(&List.flatten(&1))
    |> Enum.map(&extract_first_and_last/1)
    |> Enum.map(&List.to_string(&1))
    |> Enum.map(&String.to_integer/1)
    |> Enum.sum()
  end

  def replace_numbers(string) do
    replacements = %{
      "one" => "1",
      "two" => "2",
      "three" => "3",
      "four" => "4",
      "five" => "5",
      "six" => 6,
      "seven" => 7,
      "eight" => 8,
      "nine" => 9
    }

    pattern = ~r/(one|two|three|four|five|six|seven|eight|nine)/i

    Regex.replace(pattern, string, fn _, match ->
     "#{Map.get(replacements, String.downcase(match))}"
    end)
  end
end
