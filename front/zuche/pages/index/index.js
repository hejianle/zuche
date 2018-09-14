// pages//index.js
// pages/user/index.js
Page({
 
	/**
	 * 页面的初始数据
	 */
	data: {
		isLogin: '',
		dataList: '',
		boolean: true
	},
	login: function () {
		let that = this;
		// 登录
		wx.login({
			success: res => {
				console.log(res)
				// 发送 res.code 到后台换取 openId, sessionKey, unionId
				//获取encryptedData和iv
				let encryptedData = wx.getStorageSync('encryptedData');
				let iv = wx.getStorageSync('iv');
				let code = res.code;
				//获取用户信息
				wx.getUserInfo({
					success: function (res) {
						let encryptedData = res.encryptedData;
						let iv = res.iv;
						that.setData({
							encryptedData: encryptedData,
							iv: iv
						});
						//发送请求
						wx.request({
							url: 'https://www.muwai.com/index.php/Xcx/Login/check_wx_first',
							data: { code: code, encryptedData: encryptedData, iv: iv },
							success: res => {
								console.log(res)
								let oStatus = res.data.status;
								console.log(oStatus)
								if (oStatus == 100) {
									let isLogin1 = res.data.is_first_login;
									if (isLogin1 == 1) {
										//跳转到注册页面
										wx.redirectTo({
											url: '../register/index?code=' + code,
										})
									} else if (isLogin1 == 2) {
										//let avatarUrl = wx.getStorageSync('avatarUrl');
										wx.request({
											url: 'https://www.muwai.com/index.php/Xcx/Login/wx_login',
											data: { code: code, username: '', phone: '', password: '', phone_code: '', head_photo: '' },
											success: res => {
												//成功的话直接跳转到首页
												let oStatus = res.data.status;
												if (oStatus == 100) {
													let session_id = res.data.session_id;
													wx.setStorageSync('session_id', session_id);
 
													wx.switchTab({
														url: '../index/index?session_id=' + session_id
													})
													that.setData({
														boolean: true
													});
												}
 
 
											}
										})
									}
								} else {
									//记得以后给用户告知错误信息
									that.setData({
										info: res.data.info
									});
									//console.log(res.data.info)
								}
							}
						})
 
					}
				})
			}
		})
	},
	//登出
	loginOut: function (options) {
		let that = this;
		wx.request({
			url: 'https://www.muwai.com/index.php/Xcx/Login/login_out',
			success: res => {
				let oStatus = res.data.status;
				if (oStatus == 100) {
					wx.setStorageSync('session_id', '');
					let session_id = wx.getStorageSync('session_id');
					wx.switchTab({
						url: '../index/index?session_id=' + session_id
					});
					that.setData({
						boolean: true
					});
				}
				wx.setStorageSync('session_id', '');
			}
		})
	},
 
	/**
	 * 生命周期函数--监听页面加载
	 */
	onLoad: function (options) {
 
	},
 
	/**
	 * 生命周期函数--监听页面初次渲染完成
	 */
	onReady: function () {
 
	},
 
	/**
	 * 生命周期函数--监听页面显示
	 */
	onShow: function () {
		let session_id = wx.getStorageSync('session_id');
		console.log(session_id)
		let that = this;
		wx.request({
			url: 'https://www.muwai.com/index.php/Xcx/User/index?session_id=' + session_id,
			success: res => {
				let oStatus = res.data.status;
				if (oStatus == 100) {
					this.setData({
						isLogin: 1,
						boolean: false
					});
 
					//加载个人信息
					wx.request({
						url: 'https://www.muwai.com/index.php/Xcx/User/index?session_id=' + session_id,
						success: res => {
							console.log(res)
							let oStatus = res.data.status;
							if (oStatus == 100) {
								var data = res.data.userinfo;
								that.setData({
									dataList: data
								});
							} else if (oStatus == 101) {
 
							}
						}
					})
 
				} else if (oStatus == 101) {
					this.setData({
						isLogin: 2,
						boolean: false
					});
				}
			}
		})
 
 
	},
 
	/**
	 * 生命周期函数--监听页面隐藏
	 */
	onHide: function () {
 
	},
 
	/**
	 * 生命周期函数--监听页面卸载
	 */
	onUnload: function () {
 
	},
 
	/**
	 * 页面相关事件处理函数--监听用户下拉动作
	 */
	onPullDownRefresh: function () {
 
	},
 
	/**
	 * 页面上拉触底事件的处理函数
	 */
	onReachBottom: function () {
 
	},
 
	/**
	 * 用户点击右上角分享
	 */
	onShareAppMessage: function () {
 
	}
})
