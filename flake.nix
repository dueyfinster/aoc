{
  description = "Livebook Advent of Code";

  inputs = {
    nixpkgs = {url = "github:NixOS/nixpkgs/nixos-unstable";};
    flake-utils = {url = "github:numtide/flake-utils";};
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
  }:
    flake-utils.lib.eachDefaultSystem (system:
      with nixpkgs.legacyPackages.${system}; let
        inherit (pkgs.lib) optional optionals;
        pkgs = import nixpkgs {inherit system;};

        lbb = writeShellScriptBin "lbb" ''
          #!/usr/bin/env bash
          ${pkgs.livebook}/bin/livebook start
        '';
        lbs = writeShellScriptBin "lbs" ''
          #!/usr/bin/env bash
          ${pkgs.livebook}/bin/livebook stop
        '';
      in
        with pkgs; {
          devShell = mkShell {
            buildInputs =
              [
                alejandra
                git
                elixir
                elixir-ls
                livebook
                lbb
                lbs
                tailspin
              ]
              ++ optional stdenv.isLinux inotify-tools
              ++ optional stdenv.isDarwin terminal-notifier
              ++ optionals stdenv.isDarwin (with darwin.apple_sdk.frameworks; [
                CoreFoundation
                CoreServices
              ]);
            shellHook = ''
              mkdir -p .artifacts
              export ARTIFACT_DIR=$PWD/.artifacts
              export MIX_HOME=$ARTIFACT_DIR/mix
              export HEX_HOME=$ARTIFACT_DIR/hex
              export LIVEBOOK_HOME=$PWD
            '';
          };
        });
}
