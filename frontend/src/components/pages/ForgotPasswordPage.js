import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { Message } from 'semantic-ui-react';
import ForgotPasswordForm from '../forms/ForgotPasswordForm';
import { resetpw } from '../../actions/auth';

class ForgotPasswordPage extends React.Component{
  state ={
    success: false
  }

  submit = data => this.props
    .resetpw(data)
    .then(() => this.setState({success: true}))

  render() {
    return (
      <div>
        {this.state.success ? (
            <Message>Please check your email for instructions to reset your password.</Message>
          ) : (
            <ForgotPasswordForm submit={this.submit}/>
        )}
      </div>
    )
  }
}

ForgotPasswordPage.propTypes = {
  resetpw: PropTypes.func.isRequired
}

export default connect(null, { resetpw })(ForgotPasswordPage);
