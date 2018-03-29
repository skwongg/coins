import React from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { Form, Dropdown } from 'semantic-ui-react';
import { coinsearch } from '../../actions/coins';

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

  onChange = (e, data) => {
    this.setState({query: data.value});
    this.props.onCoinSelect(this.state.coins[data.value]);
    // this.props.onCoinSelect(this.state.coins[data.value]);
  }

  fetchOptions = () => {
    if (!this.state.query) return;
    this.setState({loading: true});
    this.props.coinsearch(this.state.query.searchQuery)
    .then(res => this.setState(res));
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
          onChange={this.onChange}
        />
      </Form>
    );
  }
}

SearchCoinForm.propTypes = {
  onCoinSelect: PropTypes.func.isRequired
}

export default connect(null, { coinsearch })(SearchCoinForm);
