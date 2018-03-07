import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { Grid, Image } from 'semantic-ui-react';
import ConfirmEmailMessage from '../messages/ConfirmEmailMessage';

const DashboardPage = ({ isConfirmed }) => (
  <Grid stackable columns={3} divided>
      <Grid.Column>
      </Grid.Column>
      <Grid.Column>
      </Grid.Column>
      <Grid.Column>
      </Grid.Column>
      {!isConfirmed && <ConfirmEmailMessage />}
  </Grid>
)

DashboardPage.propTypes = {
  isConfirmed: PropTypes.bool.isRequired
};

function mapStateToProps(state) {
  return {
    isConfirmed: !!state.user.confirmed
  };
}

export default connect(mapStateToProps)(DashboardPage);
