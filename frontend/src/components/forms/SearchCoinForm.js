import React from 'react';

class SearchCoinForm extends React.Component {
  state = {
    query: '',
    loading: false,
    options: [{
        key: 1,
        value: 1,
        text: 'first coin'
      },
      {
        key: 2,
        value: 3,
        text: 'second coin'

      }
    ],
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
        />
      </Form>
    );
  }
}

export default SearchCoinForm;
