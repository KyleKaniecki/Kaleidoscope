/**
 * Created by tabledwler on 1/25/17.
 */

$(document).ready(function() {
    $('.delete-notification').click(deleteSuccess());
});

var updateSuccess = function (response) {
    var notification_box = $(nfBoxListClassSelector);
    var notifications = response.notifications;
    $.each(notifications, function (i, notification) {
        notification_box.prepend(notification.html);
    });
};

var markSuccess = function (response, notification) {
    //console.log(response);
    if (response.action == 'read') {
        var mkClass = readNotificationClass;
        var rmClass = unreadNotificationClass;
        var action = 'unread';
    } else {
        mkClass = unreadNotificationClass;
        rmClass = readNotificationClass;
        action = 'read';
    }
    // console.log(notification.closest(nfClassSelector));
    notification.closest(nfSelector).removeClass(rmClass).addClass(mkClass);
    notification.attr('data-mark-action', action);

    toggle_text = notification.attr('data-toggle-text') || 'Mark as ' + action;
    notification.attr('data-toggle-text', notification.html());
    notification.html(toggle_text);

    alert("FUCKING BOTCHES");
};

var markAllSuccess = function (response) {
    //console.log(response);
    // console.log(response.action);
    if (response.action == 'read') {
        var mkClass = readNotificationClass;
        var rmClass = unreadNotificationClass;
    } else {
        mkClass = unreadNotificationClass;
        rmClass = readNotificationClass;
    }
    // console.log(mkClass);
    // console.log(rmClass);
    $(nfSelector).removeClass(rmClass).addClass(mkClass);
};

var deleteSuccess = function (response, notification) {
    //console.log(response);
    var $selected_notification = notification.closest(nfClassSelector);
    $selected_notification.fadeOut(300, function () {
        $(this).remove()
    });
};