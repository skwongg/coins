import axios from 'axios';
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default {
    user: {
      login: (credentials) =>
        axios.post('/api/v1/auth/', {credentials}).then(res => {
          return JSON.parse(res.data)
        }),
      signup: user =>
        axios.post('/api/v1/users/register', {user}).then(res => {
          return res.data
        }),
      verify: token =>
        axios.post('/api/v1/users/verify', {token}).then(res => {
          return res.data
        }),
      resetpw: data =>
        axios.post('/api/v1/users/resetpw', { data }).then(function(res) {
          return res.data
        }),

      resetPassword: data =>
        axios.post('/api/v1/users/newpw', {data})
    },

    coin: {
      coinsearch: querystring =>
        axios.get(`/api/v1/coins/search?q=${querystring}`)
          .then(res => res.data.hits)
          .then(coins => {
            const options = []
            const coinsHash = {};
            coins.hits.forEach(coin => {
              coinsHash[coin._id] = coin;
              options.push({
                key: coin._id,
                value: coin._id,
                ticker: coin._source.ticker,
                pair: coin._source.pair,
                name: coin._source.name,
                price: coin._source.price,
                btc_price: coin._source.btc_price,
                icon_url: coin._source.icon_url,
                text: coin._source.pair
              })
            });
            return {loading: false, options, coins: coinsHash}
          }),
    }
};
