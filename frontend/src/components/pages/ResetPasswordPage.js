import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { Message } from 'semantic-ui-react';
import ResetPasswordForm from '../forms/ResetPasswordForm';
import { resetPassword } from '../../actions/auth';
import { Link } from 'react-router-dom'



class ResetPasswordPage extends React.Component{
  state ={
    success: false
  }

  submit = data => this.props
    .resetPassword(data)
    .then(() => this.setState({success: true}))

  render() {
    const token = this.props.match.params.token;
    return (
      <div>
        {this.state.success ? (
            <Message>Your password has been reset. Login <Link to='/login'>here.</Link></Message>
          ) : (
            <ResetPasswordForm submit={this.submit} token={token} />
        )}
      </div>
    )
  }
}

ResetPasswordPage.propTypes = {
  resetPassword: PropTypes.func.isRequired
}

export default connect(null, { resetPassword })(ResetPasswordPage);
