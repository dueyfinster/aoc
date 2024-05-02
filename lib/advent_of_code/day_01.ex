# 2023 Day 1
# Started: 01/05/24
# Finished: Part 1 - 01/05/24
# Finished: Part 2 - 02/05/24
# Problem summary:
# Pt1 - Parse numbers from input, concat first/last num & add.
# Pt2 - Also convert named numbers "three"-> "3" - complication is where
# they overlap - i.e. oneight should be "18"
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
    # second pass for overlap words
    |> Enum.map(&replace_numbers/1)
    |> IO.inspect()
    |> Enum.map(&Regex.scan(~r/\d/, &1))
    |> Enum.map(&List.flatten(&1))
    |> Enum.map(&extract_first_and_last/1)
    |> Enum.map(&List.to_string(&1))
    |> Enum.map(&String.to_integer/1)
    |> Enum.sum()
  end

  def replace_numbers(string) do
    # Really hacky because we want oneight to be 18 and not 1ight
    # keep first and last letter intact so next word not impacted
    replacements = %{
      "one" => "o1e",
      "two" => "t2o",
      "three" => "t3e",
      "four" => "f4r",
      "five" => "f5e",
      "six" => "s6x",
      "seven" => "s7n",
      "eight" => "e8t",
      "nine" => "n9e"
    }

    pattern = ~r/(one|two|three|four|five|six|seven|eight|nine)/i

    Regex.replace(pattern, string, fn _, match ->
      IO.puts(string <> "/" <> match <> "/" <> Map.get(replacements, String.downcase(match)))
      "#{Map.get(replacements, String.downcase(match))}"
    end)
  end
end
