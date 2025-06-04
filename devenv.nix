{pkgs, ...}: {
  languages = {
    python.enable = true;
  };
  packages = with pkgs; [gnumake twine pipenv] ++ (with python3Packages; [setuptools wheel]);
  git-hooks.hooks = {
    alejandra.enable = true;
    black.enable = true;
    deadnix.enable = true;
    flake8.enable = true;
    isort.enable = true;
    pyupgrade.enable = true;
  };
}
