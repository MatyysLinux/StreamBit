input.onGesture(Gesture.Shake, function () {
    serial.writeLine("shake")
})
input.onPinPressed(TouchPin.P0, function () {
    serial.writeLine("p0")
})
// Handshake: přijme "test", pak ukáže "1" a ✔
serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    cmd = serial.readLine()
    if (cmd == "test") {
        serial.writeLine("OK")
        basic.showIcon(IconNames.Yes)
        basic.pause(1000)
        basic.showString("1")
    }
})
// Příkazy z tlačítek (běží až po handshake)
input.onButtonPressed(Button.A, function () {
    serial.writeLine("a")
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    serial.writeLine("logo")
})
input.onPinPressed(TouchPin.P2, function () {
    serial.writeLine("p2")
})
input.onButtonPressed(Button.AB, function () {
    serial.writeLine("ab")
})
input.onButtonPressed(Button.B, function () {
    serial.writeLine("b")
})
input.onPinPressed(TouchPin.P1, function () {
    serial.writeLine("p1")
})
let cmd = ""
serial.redirectToUSB()
