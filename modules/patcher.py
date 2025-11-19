def apply_patch(patch_json):
    changes = patch_json.get("changes", [])

    for change in changes:
        file = change["file"]
        line_number = change["line_to_replace"]
        new_line = change["new_line"]

        # Lire le fichier
        with open(file, "r") as f:
            lines = f.readlines()

        # Appliquer le patch
        lines[line_number - 1] = new_line + "\n"

        # Réécrire
        with open(file, "w") as f:
            f.writelines(lines)
