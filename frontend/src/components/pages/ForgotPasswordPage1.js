import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import ForgotPasswordForm from '../forms/ForgotPasswordForm';
import { resetpw } from '../../actions/auth';
import { Link } from 'react-router-dom';

class ForgotPasswordPage extends React.Component {
  submit = (data) =>
    this.props.resetpw(data).then(() => this.props.history.push('/dashboard'));

  render() {
    return (
      <div>
        <h1>Forgot password?</h1>
        <ForgotPasswordForm submit={this.submit}/>
      </div>
    )
  }
}

ForgotPasswordPage.propTypes = {
  history: PropTypes.shape({
    push: PropTypes.func.isRequired
  }).isRequired,
  resetpw: PropTypes.func.isRequired
}

export default connect(null, { resetpw }) (ForgotPasswordPage);
