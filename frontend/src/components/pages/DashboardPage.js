import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { Grid } from 'semantic-ui-react';
import ConfirmEmailMessage from '../messages/ConfirmEmailMessage';
import { allCoinsSelector } from '../../reducers/coins';
import AddCoinCTA from '../ctas/AddCoinCTA';

const DashboardPage = ({ isConfirmed, coins }) => (

  <div>
    {coins.length === 0 && <AddCoinCTA/>}
    <AddCoinCTA/>

    <Grid stackable columns={3} divided>
        {!isConfirmed && <ConfirmEmailMessage />}
    </Grid>
  </div>
)

DashboardPage.propTypes = {
  isConfirmed: PropTypes.bool.isRequired,
  coins: PropTypes.arrayOf(PropTypes.shape({
    name: PropTypes.string.isRequired
  }).isRequired).isRequired
};

function mapStateToProps(state) {
  return {
    isConfirmed: !!state.user.confirmed,
    coins: allCoinsSelector(state)
  };
}

export default connect(mapStateToProps)(DashboardPage);
