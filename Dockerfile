FROM python:3.11

WORKDIR /workspace
# install ml tools
RUN pip install --no-cache-dir \
numpy \
matplotlib \
jupyter \
pandas \
scikit-learn

# Expose Jupyter Port
EXPOSE 8888

# Start Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
