input.onGesture(Gesture.Shake, function () {
    serial.writeLine("shake2")
})
input.onPinPressed(TouchPin.P0, function () {
    serial.writeLine("p02")
})
// Handshake: přijme "test", pak ukáže "1" a ✔
serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    cmd = serial.readLine()
    if (cmd == "test") {
        serial.writeLine("OK")
        basic.showIcon(IconNames.Yes)
        basic.pause(1000)
        basic.showString("2")
    }
})
// Příkazy z tlačítek (běží až po handshake)
input.onButtonPressed(Button.A, function () {
    serial.writeLine("a2")
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    serial.writeLine("logo2")
})
input.onPinPressed(TouchPin.P2, function () {
    serial.writeLine("p22")
})
input.onButtonPressed(Button.AB, function () {
    serial.writeLine("ab2")
})
input.onButtonPressed(Button.B, function () {
    serial.writeLine("b2")
})
input.onPinPressed(TouchPin.P1, function () {
    serial.writeLine("p12")
})
let cmd = ""
serial.redirectToUSB()
