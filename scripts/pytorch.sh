echo BEGIN - Running in "$(pwd)"

# =====================================
# Set up Python virtual env for project.
# =====================================
# Delete venv folder if already exists
VENV_DIR=.venv
if [ -d $VENV_DIR ]; then
    START=$(date +%s%N)
    rm -Rf $VENV_DIR
    END=$(date +%s%N)
    echo VENV REMOVE: Run duration = "$(( ($END - $START) / 1000000 )) milliseconds"
fi

# Create venv
START=$(date +%s%N)
python -m venv $VENV_DIR
END=$(date +%s%N)
echo VENV CREATE: Run duration = "$(( ($END - $START) / 1000000 )) milliseconds"

# =====================================
# Activate and Update
# which python; which pip;
# =====================================
START=$(date +%s%N)
source "${VENV_DIR}/bin/activate"
python -m pip install --quiet --upgrade pip wheel setuptools
END=$(date +%s%N)
echo PIP UPDATE: Run duration = "$(( ($END - $START) / 1000000 )) milliseconds"

# =====================================
# Install Python torch package
# Note - Check TMPDIR env - ``echo $TMPDIR``
#   Run to set temp folder if needed - `TMPDIR=/opt/rspro/tmp`
#   Run to set temp folder if needed - `TMPDIR=/opt/tmpdir`
# =====================================
START=$(date +%s%N)
pip install --quiet torch
END=$(date +%s%N)
echo PYTORCH INSTALL: Run duration = "$(( ($END - $START) / 1000000 )) milliseconds"

# =====================================
# Clean up
# =====================================
deactivate
START=$(date +%s%N)
rm -Rf $VENV_DIR
END=$(date +%s%N)
echo CLEANUP: Run duration = "$(( ($END - $START) / 1000000 )) milliseconds"

echo END