#!/usr/bin/with-contenv bashio
echo "M3U Merge Service Starting.."


export M3U_USERNAME=$(bashio::config 'username')
export M3U_PASSWORD=$(bashio::config 'password')

bashio::log.info "M3U Merge Service Starting..."

# echo `echo `python3 /app/covid_il_bot/post_reddit.py $([[ $(bashio::config 'print_output') == "true" ]] && { echo "--print"; } || { echo ""; }) $([[ $(bashio::config 'post_disabled') == "true" ]] && { echo "--post-disabled"; } || { echo ""; }) $([[ $(bashio::config 'test_post') == "true" ]] && { echo "--test-post"; } || { echo ""; }) $([[ $(bashio::config 'initial_delay_seconds') -gt 0 ]] && { echo "--delay $(bashio::config 'initial_delay_seconds')"; } || { echo ""; }) $([[ $(bashio::config 'reference_date') == "" ]] && { echo ""; } || { echo "--reference-date $(bashio::config 'reference_date')"; })``
# python3 /app/covid_il_bot/post_reddit.py $([[ $(bashio::config 'print_output') == "true" ]] && { echo "--print"; } || { echo ""; }) $([[ $(bashio::config 'post_disabled') == "true" ]] && { echo "--post-disabled"; } || { echo ""; }) $([[ $(bashio::config 'test_post') == "true" ]] && { echo "--test-post"; } || { echo ""; }) $([[ $(bashio::config 'initial_delay_seconds') -gt 0 ]] && { echo "--delay $(bashio::config 'initial_delay_seconds')"; } || { echo ""; }) $([[ $(bashio::config 'reference_date') == "" ]] && { echo ""; } || { echo "--reference-date $(bashio::config 'reference_date')"; })
python3 merge-m3u.py &
python3 -m http.server 7845