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
      resetpw: (data) =>
        axios.post('/api/v1/users/resetpw', {data}).then(function(res) {
          return res.data
        })

    }
};
