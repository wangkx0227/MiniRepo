// other 其他
// message 消息
// notification-referer @我

const DrawerNotificationBut  = document.getElementById("DrawerNotificationBut") // 触发消息按钮
const NotificationContentLabel = document.getElementById("notification-content"); // 消息内容

// ajax请求，发送后端请求数据
function notificationMessageAjax(params) {
  // params：点击时的按钮id
  console.log(params);
  setTimeout(() => {
    NotificationContentLabel.innerHTML = `<s-empty>暂时没有消息</s-empty>`;
  }, 5000);
}

// 对通知选项卡设置点击事件
function createNotificationClick(notificationId) {
  const el = document.getElementById(notificationId);
  if (!el) return;
  el.addEventListener("click", () => {
    NotificationContentLabel.innerHTML = `<s-circular-progress indeterminate="true" class="notification-content-circular-progress"></s-circular-progress>`;
    notificationMessageAjax(notificationId);
  });
}

const tabNList = [
  "notification-referer",
  "notification-message",
  "notification-other",
];

// 循环生成或者说赋值点击函数
for (const id of tabNList) {
    createNotificationClick(id);
}

// 当点击触发消息按钮进行加载-@我的内容
let notificationPopupLoaded = false; // 防止多次加载
DrawerNotificationBut.addEventListener("click",()=>{
  if (!notificationPopupLoaded) {
    // 自动触发第一个 tab 的加载
    NotificationContentLabel.innerHTML = `<s-circular-progress indeterminate="true" class="notification-content-circular-progress"></s-circular-progress>`;
    notificationMessageAjax("notification-referer"); // 假设这是加载函数
    notificationPopupLoaded = true;
  }
})