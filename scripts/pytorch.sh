echo BEGIN - Running in "$(pwd)"

# =====================================
# Set up Python virtual env for project. 
# =====================================
# Delete venv folder if already exists
VENV_DIR=.venv
if [ -d $VENV_DIR ]; then
    START=$(date +%s)
    rm -Rf $VENV_DIR 
    END=$(date +%s)
    echo VENV REMOVE: Run duration = "$(date -u -d "0 $END seconds - $START seconds" +"%H:%M:%S")"
fi

# Create venv
START=$(date +%s)
python -m venv $VENV_DIR
END=$(date +%s)
echo VENV CREATE: Run duration = "$(date -u -d "0 $END seconds - $START seconds" +"%H:%M:%S")"

# =====================================
# Activate and Update
# which python; which pip;
# =====================================
START=$(date +%s)
source "${VENV_DIR}/bin/activate"
python -m pip install --quiet --upgrade pip wheel setuptools
END=$(date +%s)
echo PIP UPDATE: Run duration = "$(date -u -d "0 $END seconds - $START seconds" +"%H:%M:%S")"

# =====================================
# Install Python torch package
# Note - Check TMPDIR env - ``echo $TMPDIR``
#   Run to set temp folder if needed - `TMPDIR=/opt/rspro/tmp`
#   Run to set temp folder if needed - `TMPDIR=/opt/tmpdir`
# =====================================
START=$(date +%s)
pip install --quiet torch
END=$(date +%s)
echo PYTORCH INSTALL: Run duration = "$(date -u -d "0 $END seconds - $START seconds" +"%H:%M:%S")"

# =====================================
# Clean up
# =====================================
deactivate
START=$(date +%s)
rm -Rf $VENV_DIR   
END=$(date +%s)
echo CLEANUP: Run duration = "$(date -u -d "0 $END seconds - $START seconds" +"%H:%M:%S")"

echo END