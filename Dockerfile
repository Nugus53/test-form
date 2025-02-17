FROM jupyter/base-notebook:latest

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy repository files into the image
COPY . /home/jovyan/
WORKDIR /home/jovyan/

# Install Python dependencies if requirements.txt exists
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt || true

# Install Conda dependencies if environment.yml exists
COPY environment.yml /tmp/environment.yml
RUN conda env update --file /tmp/environment.yml --prune || true

# Expose the necessary port for Jupyter Notebook
EXPOSE 8888

# Set the default command to start Jupyter Notebook
CMD ["start-notebook.sh"]
