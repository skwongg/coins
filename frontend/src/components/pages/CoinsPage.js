import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { Grid, Container } from 'semantic-ui-react';
import { getCoins } from '../../actions/coins'
import CoinCard from '../coins/CoinCard'


class CoinsPage extends React.Component {

  componentDidMount() {
    this.props.dispatch(getCoins())
  }

  render() {
    const { coins } = this.props.coins
    return (
        <Grid container columns={2}>
          <Grid.Column >
          {coins.length > 0 ? coins.map(coin =>
              <CoinCard coin={coin}/>
            ) : null }
          </Grid.Column>
        </Grid>
    )
  }
}



CoinsPage.propTypes = {
  isConfirmed: PropTypes.bool.isRequired,
  coins: PropTypes.array.isRequired
};


const mapStateToProps = state => ({
  isConfirmed: !!state.user.confirmed,
  coins: state.coins
})

export default connect(mapStateToProps)(CoinsPage);
