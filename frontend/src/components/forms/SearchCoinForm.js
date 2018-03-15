import React from 'react';
import { Form, Dropdown } from 'semantic-ui-react';
import { login } from '../../actions/coins';
import axios from 'axios';
class SearchCoinForm extends React.Component {
  state = {
    query: '',
    loading: false,
    options: [],
    coins: {}
  }

  onSearchChange = (e, data) => {
    clearTimeout(this.timer);
    this.setState({
      query: data
    });
    this.timer = setTimeout(this.fetchOptions, 1000);
  }

  fetchOptions = () => {
    if (!this.state.query) return;
    this.setState({
      loading: true
    });
    axios.get(`/api/v1/coins/search?q=${this.state.query.searchQuery}`)
    .then(res =>
      res.data.coin
      ).then(coin => {
      const options = []
      const coinsHash = {};
      if (coin) {
          coinsHash[coin.ticker] = coin;
          options.push({
            key: coin.ticker,
            price: coin.price
          })
      }
      this.setState({loading:false, options, coins: coinsHash})
    })
  }

  render() {
    return (
      <Form>
        <Dropdown
          search
          fluid
          placeholder="Search for a coin by ticker"
          value={this.state.query}
          onSearchChange={this.onSearchChange}
          options={this.state.options}
          loading={this.state.loading}
        />
      </Form>
    );
  }
}

export default SearchCoinForm;
