FROM registry.cn-shenzhen.aliyuncs.com/stringk_python/tensorflow-gpu:py3
ENV LC_ALL C.UTF-8
ADD . /bigdata/docker_gpu_check/
RUN mkdir -p /bigdata/docker_gpu_check/logs/ \
&& rm  -rf /bigdata/docker_gpu_check/.svn && pip3 install --no-cache-dir -r /bigdata/docker_gpu_check/requirements.txt
CMD sh -c "cd /bigdata/docker_gpu_check/ && gunicorn manager:app -b 0.0.0.0:40000 -w 1 -k uvicorn.workers.UvicornWorker"