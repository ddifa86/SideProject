# image based on fluentd v1.14-1
FROM fluentd:v1.14-1

# Use root account to use apk
USER root

# 리포지토리 미러 변경 및 패키지 설치
RUN sed -i 's|dl-cdn.alpinelinux.org|mirror.leaseweb.com|' /etc/apk/repositories \
    && apk add --no-cache \
    build-base \
    openssl-dev

# 호환 가능한 버전의 faraday 설치 후 Elasticsearch 플러그인 설치
RUN gem install faraday -v 2.8.1 \
    && gem install faraday-net_http -v 3.0.2 \
    && gem install elasticsearch -v 7.17.0 \
    && gem install fluent-plugin-elasticsearch \
    && apk del build-base

# Fluentd 설정 복사
COPY config/fluent.conf /fluentd/etc/fluent.conf

USER fluent

CMD ["fluentd", "-c", "/fluentd/etc/fluent.conf", "-p", "/fluentd/plugins"]
