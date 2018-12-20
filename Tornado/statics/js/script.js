//主要实现：获取表单中id指分别为username何password所输入的指,alter()弹出菜单提示
$(document).ready(funtion(){
	alter("good");
	$("#login").click(funtion(){
		var user = $("#username").val();
		var pwd = $("#password").val();
		alter("username:"+user);
	});
});