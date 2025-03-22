import { NavigationMenu, NavigationMenuItem, NavigationMenuList } from "@/components/ui/navigation-menu";
import Link from "next/link";
import { LucideMenu } from "lucide-react"
import { Drawer, DrawerClose, DrawerContent, DrawerFooter, DrawerHeader, DrawerTitle, DrawerTrigger, } from "@/components/ui/drawer"
import { pageLinks } from "@/lib/page-links";
import { SearchBarComp } from "./search";
import { Button } from "../ui/button";

/**
 * The Global Navbar component 
 */
export function NavbarComp() {
    const pages: { title: string, link: string }[] = [
        { title: "Home", link: pageLinks.nav.home },
        { title: "Services", link: pageLinks.resource.contact },
        { title: "Pricing", link: pageLinks.nav.about },
        { title: "About", link: pageLinks.nav.about },
        { title: "Contacts", link: pageLinks.resource.contact },
    ]
    return (
        <>
            <nav className="flex items-center justify-between bg-white w-full border-b border-b-border/20  z-50 h-16 overflow-hidden fixed px-5">

                {/*SECTION - Logo */}
                <div className="flex items-center space-x-4">
                    {/*!SECTION */}

                    {/*SECTION - Desktop Menu Bar */}
                    <NavigationMenu className="hidden lg:flex">
                        <NavigationMenuList>
                            <NavigationMenuItem className="group space-x-5 text-sm text-neutral-900">
                                {pages.map((item, index) => (
                                    <Link className="py-2 px-3 hover:bg-background rounded-full" href={item.link} key={index}>{item.title}</Link>
                                ))}
                            </NavigationMenuItem>
                        </NavigationMenuList>
                    </NavigationMenu>
                </div>
                {/*!SECTION */}

                {/*SECTION - Navigation Side View*/}
                <NavigationMenu className="right-0">
                    <NavigationMenuList>
                        <NavigationMenuItem className="group space-x-5 flex-row">
                            {/* Navigation Menu Mobile bar*/}
                            <Drawer>
                                <div className="flex-row flex items-center space-x-2">
                                    <SearchBarComp />
                                    <Link href={pageLinks.auth.login} passHref>
                                        <Button>Log In</Button>
                                    </Link>
                                    <Link href={pageLinks.auth.signup} passHref>
                                        <Button variant={"outline"} >Sign Up</Button>
                                    </Link>
                                    <DrawerTrigger className="flex lg:hidden"><LucideMenu /></DrawerTrigger>
                                </div>
                                <DrawerContent className="border-t">
                                    <div className="mx-auto md:w-5/6 w-full overflow-y-scroll no-scrollbar">
                                        <DrawerHeader className="space-y-1">
                                            <DrawerTitle></DrawerTitle>
                                            {pages.map((item, index) => (
                                                <Link href={item.link} className="bg-primary text-white rounded-md px-4 py-2" key={index}>{item.title}</Link>
                                            ))}
                                        </DrawerHeader>
                                        <DrawerFooter>
                                            <DrawerClose>
                                            </DrawerClose>
                                        </DrawerFooter>
                                    </div>
                                </DrawerContent>
                            </Drawer>
                        </NavigationMenuItem>
                    </NavigationMenuList>
                </NavigationMenu>
                {/*!SECTION */}

            </nav >
        </>
    )
}